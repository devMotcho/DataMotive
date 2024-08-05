
document.addEventListener('DOMContentLoaded', function () {
                                
    var labels = stocks.map(stock => stock.product__name);
    var data = stocks.map(stock => stock.quantity);
    
    var ctx = document.getElementById('myChart').getContext('2d');
    
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Products In Stock',
                data: data,
                backgroundColor: 'rgba(255,193,0, 0.3)',
                borderColor: 'rgb(255,193,0, 1)',
                borderWidth: 3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: 'white' // Set y-axis labels to white
                    }
                },
                x: {
                    ticks: {
                        color: 'white' // Set x-axis labels to white
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: 'white' // Set legend font color to white
                    }
                },
                title: {
                    display: true,
                    text: 'Product Stock Distribution',
                    color: 'white' // Set title font color to white
                },
                tooltip: {
                    bodyFont: {
                        color: 'white' // Set tooltip font color to white
                    }
                }
            }
        }
    });
});