function renderStockChart(data) {
    var ctx = document.getElementById('stockChart').getContext('2d');
    var stockChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: [data.productName, 'Other Products'],
            datasets: [{
                label: 'Stock Distribution',
                data: [data.productQuantity, data.totalQuantity - data.productQuantity],
                backgroundColor: [
                    'rgba(0, 255, 0, 0.2)',
                    'rgba(255,193,0, 0.3)'
                ],
                borderColor: [
                    'rgba(0, 255, 0, 1)',
                    'rgb(255,193,0, 1)'
                ],
                borderWidth: 3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
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
}


