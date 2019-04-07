const nazwaInput = document.querySelector('input[name=nazwa]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {

    return val.toString().toLowerCase().trim()
        .replace(/_/g, Math.floor(Math.random() * 10))         
        .replace(/[\s\W-]+/g, '-') 
	

};

nazwaInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(nazwaInput.value));
});