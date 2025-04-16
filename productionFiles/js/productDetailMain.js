
// Quantity controls
function increaseQuantity() {
    const input = document.getElementById('inputQuantity');
    input.value = parseInt(input.value) + 1;
}

function decreaseQuantity() {
    const input = document.getElementById('inputQuantity');
    if (parseInt(input.value) > 1) {
        input.value = parseInt(input.value) - 1;
    }
}

// Size selection
function selectSize(size, el) {
    document.querySelectorAll('.size-btn').forEach(btn => btn.classList.remove('selected'));
    el.classList.add('selected');
}

// Slideouts
const cartNav = document.getElementById('cartNav');
const cartSlideout = document.getElementById('cartSlideout');
const menuSlideout = document.getElementById('menuSlideout');
const menuNav = document.getElementById('menu-btn');
const closeCartSlideout = document.getElementById('closeCartSlideout');
const closeMenuSlideout = document.getElementById('closeMenuSlideout');
const overlay = document.getElementById('overlay');

cartNav.addEventListener('click', () => {
    cartSlideout.style.right = "0";
    overlay.classList.add('active');
});

menuNav.addEventListener('click', () => {
    menuSlideout.style.left = "0";
    overlay.classList.add('active');
});

closeCartSlideout.addEventListener('click', () => {
    cartSlideout.style.right = "-100%";
    overlay.classList.remove('active');
});

closeMenuSlideout.addEventListener('click', () => {
    menuSlideout.style.left = "-100%";
    overlay.classList.remove('active');
});

overlay.addEventListener('click', () => {
    menuSlideout.style.left = "-100%";
    cartSlideout.style.right = "-100%";
    overlay.classList.remove('active');
});

// Format price
function formatPrice(price) {
    const num = Number(price);
    if (isNaN(num)) return 'GH₵0.00';
    return 'GH₵' + num.toFixed(2);
}


// Get total items for display
function getCartTotalItems(cart) {
    return cart.reduce((sum, item) => sum + Number(item.quantity), 0);
}

// Display cart items
function displayCartItems() {
    const cartBox = document.getElementById('cartBox');
    cartBox.innerHTML = '';
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let totalPrice = 0;

    document.getElementById('cartNav').textContent = `Cart(${getCartTotalItems(cart)})`;

    if (cart.length > 0) {
        cart.forEach(item => {
            const cartItemDiv = `
            <div class="cart-item" style="padding: 10px; margin: 10px; display: flex; align-items: center; position: relative;">
                <img src="${item.image_url}" alt="Product Image" width="100" style="border-radius: 8px; margin-right: 15px;">
                <div style="flex: 1;">
                    <div style="display:flex; gap:5px;">
                        <p style="margin: 0; font-weight: bold; font-size: 14px;">${item.product_name}</p>
                        <p style="margin: 0; font-size: 14px;">x${item.quantity}</p>
                    </div>
                    <div style='display:flex; justify-content:space-between;'>
                        <p style="margin: 0; font-size: 14px;">${item.selectedSize}</p>
                        <p style="margin: 0; font-size: 14px;">GH₵ ${item.price}</p>
                    </div>
                </div>
                <button class="close-button" onclick="removeFromCart('${item.product_id}', '${item.selectedSize}')" style="position: absolute; top: 10px; right: 10px; background: transparent; border: none; cursor: pointer; font-size: 16px; color: #FF5722;">&times;</button>
            </div>`;
            cartBox.innerHTML += cartItemDiv;
            totalPrice += item.price;
        });

        cartBox.innerHTML += `
            <div style="display: flex; justify-content: space-between; align-items: center;margin-left: 20px;">
                <div>Total:</div>
                <div class="total-price" style="color: #28a745; font-weight: bold; margin-right: 20px;">${formatPrice(totalPrice)}</div>
            </div>
            <div style="text-align: center; margin: 20px;">
                <a href="{% url 'checkout' %}">
                    <button style="padding: 10px 20px; width:100%; background-color: #228B22; color: white; border: none; border-radius: 5px; cursor: pointer;">
                        Checkout
                    </button>
                </a>
            </div>
            <div style="width:100%; height:150px;"></div>`;
    } else {
        cartBox.innerHTML = '<div class="empty-cart">Nothing in Cart</div>';
    }
}

// Remove item from cart
function removeFromCart(productId, size) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => !(item.product_id === productId && item.selectedSize === size));
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCartItems();
}

// Add to cart logic
window.onload = () => {
    displayCartItems();

    const addToCartDiv = document.getElementById('addToCartDiv');
    const product_id = '{{product.unique_id}}';
    const image_url = '{{product.image.url}}';
    const product_name = '{{product.name}}';

    addToCartDiv.onclick = () => {
        const quantity = parseInt(document.getElementById('inputQuantity').value);
        const selectedBox = document.querySelector('.size-btn.selected');
        const selectedSize = selectedBox ? selectedBox.innerText : null;

        if (!selectedSize) {
            return alert('Please select a size.');
        }

        const price = quantity * {{ product.price }};

        const newItem = {
            product_id,
            product_name,
            quantity,
            image_url,
            selectedSize,
            price
        };

        let cart = JSON.parse(localStorage.getItem('cart')) || [];

        const existingIndex = cart.findIndex(item => item.product_id === product_id && item.selectedSize === selectedSize);

        if (existingIndex !== -1) {
            cart[existingIndex] = newItem;
            alert('Updated product in cart');
        } else {
            cart.push(newItem);
            alert('Item added to cart');
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        displayCartItems();
    };
};

// Main image swap
const mainImage = document.getElementById('mainImage');
const sideImages = document.querySelectorAll('.sideImage');
sideImages.forEach(side => {
    side.onclick = function () {
        mainImage.src = side.querySelector('img').src;
    };
});


