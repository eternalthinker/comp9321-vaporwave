
function episodeChart() {
  const width = 940;
  const height = 600;

  const tooltip = floatingTooltip('character_tooltip', 240);
  const center = {
    x: width / 2,
    y: height /2
  };  

  const forceStrength = 0.03;

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
    .on('tick', ticked);

  simulation.stop();

  const strokeColor = d3.scaleOrdinal()
    .domain(['alive', 'dead'])
    .range(['#ffffff', '#000000']);

  const fillColor = d3.scaleOrdinal()
    .domain(['stark', 'targaryen', 'lannister', 'dothraki'])
    .range(['#d84b2a', '#beccae', '#7aa25c', '#cccccc']);

  function createNodes(rawData) {
    const maxEpisodes = d3.max(rawData, (d) => +d.num_episodes);

    const radiusScale = d3.scalePow()
      .exponent(0.5)
      .range([2, 50])
      .domain([0, maxEpisodes]);

    const myNodes = rawData.map((d) => {
      return {
        slug: d.slug,
        name: d.name,
        house: d.house,
        value: d.num_episodes,
        id: d.slug,
        isAlive: d.is_alive,
        radius: radiusScale(+d.num_episodes),
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
      .data(nodes, (d) => d.slug);

    function aliveStatus(isAlive) {
      if (isAlive) {
        return "alive";
      } else {
        return "dead";
      }
    }

    const bubblesE = bubbles.enter().append('circle')
      .classed('bubble', true)
      .attr('r', 0)
      .attr('fill', function (d) { return fillColor(d.house); })
      .attr('stroke', function (d) { return d3.rgb(fillColor(d.house)).darker(); })
      .attr('stroke-width', 2)
      .attr('stroke-dasharray', (d) => d.isAlive? "": "5")
      .on('mouseover', showDetail)
      .on('mouseout', hideDetail);

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
                  '<span class="name">Value: </span><span class="value">' +
                  d.value +
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

$(document).ready(function () {

  $(".button").click(function (event) {
    event.preventDefault();
    $(this).toggleClass('active').siblings().removeClass('active');
    const buttonId = $(this).attr('id');
    fetch(`data/data-${buttonId}.json`)
      .then(res => res.json())
      .then(json => display(json));
  });

  fetch(`data/data-s01e01.json`)
    .then(res => res.json())
    .then(json => display(json));

});
