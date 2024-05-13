fetch('/accounts/api/profile/',{
    method: 'GET',
    headers: {
        'Authorization': 'JWT ' + localStorage.getItem('access_token'),
        'Content-Type': 'application/json',
    },
})
.then(response => response.json())
.then(data => {
    document.getElementById('image-user').innerHTML = `<img src=${data.queryset.image} alt="Admin" class="rounded-circle" width="150">
    <div class="mt-3">
      <h4>${data.queryset.first_name} ${data.queryset.last_name}</h4>
    </div>`;
})
.catch(error => console.error('Error fetching user data:', error));
function addAddress() {
const formData = new FormData(document.getElementById("myForm-address"));
const data = {
    province: formData.get('province'),
    city: formData.get('city'),
    detailed_address: formData.get('detailed_address'),
    postal_code: formData.get('postal_code'),
};
fetch('/accounts/api/add_address/', {
    method: 'POST',
    headers: {
        'Authorization': 'JWT ' + localStorage.getItem('access_token'),
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    
})
}
