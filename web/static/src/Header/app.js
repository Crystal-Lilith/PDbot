const Selector = () => {
    const sel = document.querySelector('.selector');
    const nav = document.querySelector('.nav__links');

    const selAll = document.querySelector('.selector');

    sel.addEventListener('click', () => {
        nav.classList.toggle('togl');
        selAll.classList.toggle('toggle');
    })
}

Selector();