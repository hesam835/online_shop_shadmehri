document.addEventListener('DOMContentLoaded', function() {
    fetch('/accounts/api/address/',{
        method: 'GET',
        headers: {
            'Authorization': 'JWT ' + localStorage.getItem('access_token'),
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
      data.queryset.forEach(function(product) {
                let row = document.createElement('tr');
                row.innerHTML = '<td>' +product.province +'</td>' +
                                '<td>' + product.city + '</td>' +
                                '<td>' + product.detailed_address + '</td>' +
                                '<td>' + product.postal_code + '</td>'+
                                '<td><a href="edit_address/'+product.id+' '+'" class="btn btn-primary">edit</a></td>' ;
                document.getElementById('cart-items').appendChild(row);
            });
        });
  
});