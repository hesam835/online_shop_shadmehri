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
    document.getElementById('address-edit').innerHTML = `<form class="user" id="myForm-address">
    <div class="row mb-3">
        <div class="col-sm-3">
            <h6 class="mb-0">province</h6>
        </div>
        <div class="col-sm-9 text-secondary">
            <input type="text" class="form-control" name="province" value=${product.province}>
        </div>
    </div>
    <div class="row mb-3">
        <div class="col-sm-3">
            <h6 class="mb-0">city</h6>
        </div>
        <div class="col-sm-9 text-secondary">
            <input type="text" class="form-control" name="city" value=${product.city}>
        </div>
    </div>
    <div class="row mb-3">
        <div class="col-sm-3">
            <h6 class="mb-0">detail address</h6>
        </div>
        <div class="col-sm-9 text-secondary">
            <input type="text" class="form-control" name="detailed_address" value=${product.detailed_address}>
        </div>
    </div>
    <div class="row mb-3">
        <div class="col-sm-3">
            <h6 class="mb-0">postal code</h6>
        </div>
        <div class="col-sm-9 text-secondary">
            <input type="text" class="form-control" name="postal_code" value=${product.postal_code}>
        </div>
    </div>
    <button id="save" class="btn btn-primary d-block btn-user w-100" type="submit" onclick="editAddress()">Save address</button>
</form>`
    ;
})})
.catch(error => console.error('Error fetching address data:', error));
function editAddress() {
const formData = new FormData(document.getElementById("myForm-address"));
const data = {
    province: formData.get('province'),
    city: formData.get('city'),
    detailed_address: formData.get('detailed_address'),
    postal_code: formData.get('postal_code'),
};
fetch(window.location.pathname+'/api/', {
    method: 'PUT',
    headers: {
        'Authorization': 'JWT ' + localStorage.getItem('access_token'),
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})}