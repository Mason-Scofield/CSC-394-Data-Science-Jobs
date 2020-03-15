var color_index = 0
var colors = [
    '#EC7063',
    '#3498DB',
    '#F7DC6F',
    '#D2B4DE'
];

export function graphInit(chart, id, graphData) {
    var context = document.getElementById(id);

    color_index = 0;
    graphData.datasets.map(dataset => { dataset['backgroundColor'] = colors[color_index]; ++color_index; })

    chart = new Chart(context, {
        type: 'bar',
        data: {
            labels: graphData.labels,
            datasets: graphData.datasets
        },
        options: {
            legend: { labels: { fontSize: 15 } },
            scales: {
                xAxes: [{
                    stacked: true,
                    ticks: { fontSize: 15 }
                 }],
                yAxes: [{
                    stacked: true,
                    ticks: { fontSize: 20 }
                 }]
            },
            tooltips: {
                callbacks: {
                    title: function(tooltipItem, data) {
                          return '';
                    }
                }
            }
        }
    });
    return chart;
}


export function drawGraph(chart, graphData) {
    chart.data.labels  = graphData.labels;
    color_index = 0;
    graphData.datasets.map(dataset => { dataset['backgroundColor'] = colors[color_index]; ++color_index; })
    chart.data.datasets = graphData.datasets;
    chart.update();
}


document.getElementById('switch-slider').addEventListener('click', (e) => {
    var c1 = document.getElementById('chart1');
    var c2 = document.getElementById('chart2');
    var c1Label = document.getElementById('chart1Label');
    var c2Label = document.getElementById('chart2Label');

    if (c1.style.display === 'none') {
      c1.style.display = 'block';
      c2.style.display = 'none';
      c1Label.style.opacity = '1';
      c2Label.style.opacity = '.45';
    }
    else {
      c2.style.display = 'block';
      c1.style.display = 'none';
      c2Label.style.opacity = '1';
      c1Label.style.opacity = '.45';
    }
});
