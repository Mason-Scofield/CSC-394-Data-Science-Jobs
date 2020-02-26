$(document).ready(function() {
  var HORIZONTAL = false;
  var STACKED = false;

  var TITLE = 'Data Science';

  var LABELS = 'Keyword';  // Column to define  x axis

  var SERIES = [
    {
      column: 'Indeed',
      name: 'Keyword',
      color: 'black'
    },

    {
      column: 'Indeed',
      name: 'SimplyHired',
      color: 'blue'
    }

  ];

  var X_AXIS = 'Skills';  // x-axis label
  var Y_AXIS = 'Python'; // y-axis label

  var SHOW_GRID = true; // To show the grid
  var SHOW_LEGEND = true; // To show the legends

  // D3 to read data from csv and then map it to the values to make a chart
  d3.csv("../static/data.csv").then(function(rows) {
    console.log(rows);

    var datasets = SERIES.map(function(el) {
      return {
        label: el.name,
        labelDirty: el.column,
        backgroundColor: el.color,
        data: []
      }
    });

    rows.map(function(row) {
      datasets.map(function(d) {
        d.data.push(row[d.labelDirty])
      })
    });

		var barChartData = {
      labels: rows.map(function(el) { return el[LABELS] }),
			datasets: datasets
    };

    var ctx = document.getElementById('container').getContext('2d');

    new Chart(ctx, {
      type: HORIZONTAL ? 'horizontalBar' : 'bar',
      data: barChartData,

      options: {
        title: {
          display: true,
          text: TITLE,
          fontSize: 20,
        },
        legend: {
          display: SHOW_LEGEND,
        },
        scales: {
          xAxes: [{
            stacked: STACKED,
            scaleLabel: {
              display: X_AXIS !== '',
              labelString: X_AXIS
            },
            gridLines: {
              display: SHOW_GRID,
            },
            ticks: {
              beginAtZero: true,
              callback: function(value, index, values) {
                return value.toLocaleString();
              }
            }
          }],
          yAxes: [{
            stacked: STACKED,
            beginAtZero: true,
            scaleLabel: {
              display: Y_AXIS !== '',
              labelString: Y_AXIS
            },
            gridLines: {
              display: SHOW_GRID,
            },
            ticks: {
              beginAtZero: true,
              callback: function(value, index, values) {
                return value.toLocaleString()
              }
            }
          }]
        },
        tooltips: {
          displayColors: false,
          callbacks: {
            label: function(tooltipItem, all) {
              return all.datasets[tooltipItem.datasetIndex].label
                + ': ' + tooltipItem.yLabel.toLocaleString();
            }
          }
        }
      }
    });
  });
});