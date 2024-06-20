//Filtro
document.getElementById('searchInput').addEventListener('keyup', function() {
    var input = this.value.toLowerCase();
    var carCards = document.querySelectorAll('.car-card');

    carCards.forEach(function(card) {
        var carName = card.querySelector('.car-name').textContent.toLowerCase();
        var carMarca = card.querySelector('.car-marca').textContent.toLowerCase();
        var carPrecio = card.querySelector('.car-precio').textContent.toLowerCase();
        var carColor = card.querySelector('.car-color').textContent.toLowerCase();

        if (carName.includes(input)) {
            card.style.display = 'block';
        } else if(carMarca.includes(input)){
            card.style.display = 'block';
        }else if(carPrecio.includes(input)){
            card.style.display = 'block';
        }else if(carColor.includes(input)){
            card.style.display = 'block'
        }else{
            card.style.display = 'none';
        }
        
    });
});

// Navegation Bar
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('filter-button').addEventListener('click', function () {
        var navMenu = document.getElementById('navbar-sticky');
        navMenu.classList.toggle('hidden');
    });
});
