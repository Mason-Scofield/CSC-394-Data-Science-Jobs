var chart;

export function graphInit(graphData) {
    var context = document.getElementById('chart');
    chart = new Chart(context, {
        // bar chart
        type: 'bar',
        data: {
            labels: graphData.labels,
            datasets: [
            {
                label: graphData.dataset[0].source,
                data: graphData.dataset[0].data,
                backgroundColor: '#82E0AA'
            },
            {
                label: graphData.dataset[1].source,
                data: graphData.dataset[1].data,
                backgroundColor: '#3498DB'
            }]
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
};

export function drawGraph(graphData) {
    chart.data.labels = graphData.labels;

    var i = 0;
    chart.data.datasets.forEach(function(dataset) {
        dataset.data  = graphData.dataset[i].data;
        ++i;
    });

    chart.update();
}
