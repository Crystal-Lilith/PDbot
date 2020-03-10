const Cta = () => {
    if (login_status) {
        const logButton = document.querySelector('.cta');
        let userName = logButton.textContent;

        logButton.addEventListener('mouseover', () => {
            logButton = 'Logout';
        })

        logButton.addEventListener('mouseout', () => {
            logButton = userName;
        })

        logButton.addEventListener('click', () => {
            alert('Are you sure?');
        })
    }
}

Cta();
