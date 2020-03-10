const Cta = () => {
    const logButton = document.querySelector('.cta');
    let userName = logButton.textContent;

    logButton.addEventListener('mouseenter', () => {
        logButton = 'Logout';
    })

    logButton.addEventListener('mouseover', () => {
        logButton = userName;
    })
}

Cta();