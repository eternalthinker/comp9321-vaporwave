
function episodeChart() {
  const width = 940;
  const height = 550;

  const tooltip = floatingTooltip('character_tooltip', 240);
  const center = {
    x: width / 2,
    y: height /2
  };  

  const forceStrength = 0.06;

  let svg = null;
  let bubbles = null;
  let nodes = [];

  function charge(d) {
    return -Math.pow(d.radius, 2.1) * forceStrength;
  }

  let simulation = d3.forceSimulation()
    .velocityDecay(0.2)
    .force('x', d3.forceX().strength(forceStrength).x(center.x))
    .force('y', d3.forceY().strength(forceStrength).y(center.y))
    .force('charge', d3.forceManyBody().strength(charge))
    .force('link', d3.forceLink().id(function(d) { return d.index; }))
    .force('collide', d3.forceCollide(d => d.r + 10).iterations(24))
    .on('tick', ticked);

  simulation.stop();

  const strokeColor = d3.scaleOrdinal()
    .domain(['alive', 'dead'])
    .range(['#ffffff', '#000000']);

  const fillColor = d3.scaleOrdinal()
    .domain(['stark', 'targaryen', 'lannister', 'dothraki'])
    .range(['#d84b2a', '#beccae', '#efe40e', '#cccccc']);

  function getHouse(allegiances) {
    if (allegiances == 'NULL') {
      return 'Other';
    }
    const houseTitle = allegiances.split(',')[0];
    const house = houseTitle.split(' ')[1];
    return house;
  }

  function createNodes(rawData) {
    const maxEpisodes = d3.max(rawData, (d) => +d.episodeCount);

    const radiusScale = d3.scalePow()
      .exponent(0.5)
      .range([2, 30])
      .domain([0, maxEpisodes]);

    const myNodes = rawData.map((d) => {
      return {
        slug: d.CID,
        name: d.name,
        actor: d.actor,
        house: getHouse(d.allegiances),
        value: d.episodeCount,
        id: d.CID,
        isAlive: Boolean(d.isAlive),
        radius: radiusScale(+d.episodeCount),
        x: Math.random() * 900,
        y: Math.random() * 800
      };
    });

    myNodes.sort(function (a, b) { return b.value - a.value; });

    return myNodes;
  }

  const chart = function chart(selector, rawData) {
    nodes = createNodes(rawData);

    if (svg) {
      d3.selectAll("svg").remove();
    }
    svg = d3.select(selector)
      .append('svg')
      .attr('width', width)
      .attr('height', height);

    bubbles = svg.selectAll('.bubble')
      .data(nodes, (d) => d.CID);

    function aliveStatus(isAlive) {
      if (isAlive) {
        return "alive";
      } else {
        return "dead";
      }
    }

    function dragstarted(d) {
      if (!d3.event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }
    
    function dragged(d) {
      d.fx = d3.event.x;
      d.fy = d3.event.y;
    }
    
    function dragended(d) {
      if (!d3.event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    } 

    const bubblesE = bubbles.enter().append('circle')
      .classed('bubble', true)
      //.attr('r', 0)
      .attr('fill', function (d) { return fillColor(d.house); })
      .attr('stroke', function (d) { return d3.rgb(fillColor(d.house)).darker(); })
      .attr('stroke-width', 2)
      .attr('stroke-dasharray', (d) => d.isAlive? "": "5")
      .on('mouseover', showDetail)
      .on('mouseout', hideDetail)
      .attr("r", function(d){  return d.r })
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended))
      ;

    bubbles = bubbles.merge(bubblesE);

    bubbles.transition()
      .duration(2000)
      .attr('r', function (d) { return d.radius; });

    simulation.nodes(nodes);

    groupBubbles();
  };

  function ticked() {
    bubbles
      .attr('cx', function (d) { return d.x; })
      .attr('cy', function (d) { return d.y; });
  }

  function groupBubbles() {
    simulation.force('x', d3.forceX().strength(forceStrength).x(center.x));
    simulation.alpha(1).restart();
  }

  function showDetail(d) {
    d3.select(this).attr('stroke', 'black');

    var content = '<span class="name">Name: </span><span class="value">' +
                  d.name +
                  '</span><br/>' +
                  '<span class="name">House: </span><span class="value">' +
                  d.house +
                  '</span><br/>' +
                  '<span class="name">Actor: </span><span class="value">' +
                  d.actor +
                  '</span>';
    tooltip.showTooltip(content, d3.event);
  }

  function hideDetail(d) {
    d3.select(this)
      .attr('stroke', d3.rgb(fillColor(d.house)).darker());

    tooltip.hideTooltip();
  }

  return chart;
}

const gotChart = episodeChart();

function display(data) {
  gotChart('#vis', data);
}

function callApi({endpoint, method, data}) {
  let params = {};
  if (method === 'POST') {
    params = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    };
  }
  return fetch(endpoint, params)
    .then(res => res.json())
    .then(json => json);
}

function mashUp(episodeCharacters, characterQuotes, charactersIaF) {
  const episodeCharactersMap = episodeCharacters.reduce((acc, charInfo) => {
    acc[charInfo.CID] = charInfo;
    return acc;
  }, {});
  
  const characterQuotesMap = characterQuotes.reduce((acc, quote) => {
    const slug = quote.CID;
    if (!acc.hasOwnProperty(slug)) {
      acc[slug] = [];
    }
    acc[slug].push(quote.quote_text);
    return acc;
  }, {});

  const charactersIaFMap = charactersIaF.reduce((acc, charInfo) => {
    acc[charInfo.slug] = charInfo;
    return acc;
  }, {});

  const characters = charactersIaF.map(charInfo => {
    const slug = charInfo.slug;
    return {
      ...charInfo,
      ...episodeCharactersMap[slug],
      quotes: characterQuotes[slug]
    }
  });

  /*const characters = episodeCharacters.map(charInfo => {
    const slug = charInfo.CID;
    return {
      ...charInfo,
      ...charactersIaFMap[slug],
      quotes: characterQuotesMap[slug]
    }
  });*/

  return characters;
}

function loadEpisode(seasonNumber, episodeNumber) {
  callApi({
    endpoint: `http://localhost:5000/season/${seasonNumber}/episode/${episodeNumber}/characters`,
    method: 'GET'
  })
  .then(episodeCharacters => {
    callApi({
      endpoint: `http://localhost:5000/season/${seasonNumber}/episode/${episodeNumber}/quotes`,
      method: 'GET'
    })
    .then(characterQuotes => {
      const characterList = episodeCharacters.map(charInfo => charInfo.CID);
      callApi({
        endpoint: `http://localhost:7000/characters`,
        method: 'POST',
        data: characterList
      })
      .then(charactersIaF => {
        const characters = mashUp(episodeCharacters, characterQuotes, charactersIaF);
        console.log(characters);
        display(characters);
      }); // IaF - characters
    }); // IMDB - quotes
  }); // IMDB - episode chars
}

function getEID(seasonNumber, episodeNumber) {
  return `${("0" + seasonNumber).slice(-2)}${("0" + episodeNumber).slice(-2)}`;
}

function showTimelineProgress(seasonNumber, episodeNumber) {
  $('.episode-step').removeClass('form-steps__item--active');
  Array.from(Array(seasonNumber-1).keys()).forEach((s) => {
    Array.from(Array(10).keys()).forEach((e) => {
      const eid = getEID(s+1, e+1);
      const stepEl = $(`#episode-step-${eid}`)
      if (stepEl) {
        stepEl.addClass('form-steps__item--active');
      }
    });
  });
  Array.from(Array(episodeNumber).keys()).forEach((e) => {
    const eid = getEID(seasonNumber, e+1);
    $(`#episode-step-${eid}`).addClass('form-steps__item--active');
  });
}

function displayEpisodeTimeline(episodes) {
  episodes = episodes.sort((e1, e2) => {
    if (e1.seasonNumber === e2.seasonNumber) {
      return +e1.episodeNumber - +e2.episodeNumber;
    }
    return +e1.seasonNumber - +e2.seasonNumber;
  });

  $episodeTimeline = $("#episode-timeline");

  episodes.forEach((episode, i) => {
    const episodeNumber = +episode.episodeNumber;
    const seasonNumber = +episode.seasonNumber;
    let seasonText = '.';
    if (episodeNumber === 1) {
      seasonText = `S${episode.seasonNumber}`;
    }
    $episodeStep = $(`<div id="episode-step-${episode.EID}" class="episode-step form-steps__item">
        <div class="form-steps__item-content">
          <span class="form-steps__item-icon">${episodeNumber}</span>
          <span class="form-steps__item-line"></span>
          <span class="form-steps__item-text">${seasonText}</span>
        </div>
      </div>`
    );
    if (i === 0) {
      $episodeStep.addClass('form-steps__item--active');
      $episodeStep.find('.form-steps__item-line').remove();
    }

    $episodeStep.click(event => {
      loadEpisode(seasonNumber, episodeNumber);
      showTimelineProgress(seasonNumber, episodeNumber);
    });

    $episodeTimeline.append($episodeStep)
  });
}



$(document).ready(function () {

  $(".button").click(function (event) {
    event.preventDefault();
    $(this).toggleClass('active').siblings().removeClass('active');
    const buttonId = $(this).attr('id');
    fetch(`data/data-${buttonId}.json`)
      .then(res => res.json())
      .then(json => display(json));
  });

  fetch(`http://localhost:5000/episodes`)
    .then(res => res.json())
    .then(json => displayEpisodeTimeline(json));

  loadEpisode(1, 1);

  /*fetch(`data/data-s01e01.json`)
    .then(res => res.json())
    .then(json => display(json));*/

});
