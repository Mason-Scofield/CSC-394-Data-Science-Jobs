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
};

export function drawGraph(chart, graphData) {
    chart.data.labels  = graphData.labels;
    color_index = 0;
    graphData.datasets.map(dataset => { dataset['backgroundColor'] = colors[color_index]; ++color_index; })
    chart.data.datasets = graphData.datasets;
    chart.update();
}
