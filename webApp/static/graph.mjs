function graphInit(data) {
    console.log(data)
    var context   = document.getElementById('chart');
    var chart = new Chart(context, {
        // bar chart
        type: 'bar',
        data: {
            labels: ['HTML, CSS, & JavaScript', 'Python', 'R', 'SQL'],
            datasets: [
            {
                label: 'GitHub Jobs',
                data: [10, 20, 30, 40],
                backgroundColor: '#D6E9C6'
            },
            {
                label: 'USA Jobs',
                data: [10, 20, 30, 40],
                backgroundColor: '#FAEBCC'
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    stacked: true,
                }],
                yAxes: [{
                    stacked: true,
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
});
