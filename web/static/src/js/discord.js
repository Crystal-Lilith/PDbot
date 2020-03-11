function loginCheck() {
    let logButton = document.querySelector('.cta');
    let userName = logButton.text;

    logButton.addEventListener('mouseover', () => {
        logButton.text = 'Logout';
    })

    logButton.addEventListener('mouseout', () => {
        logButton.text = userName;
    })

    logButton.addEventListener('click', () => {
        alert('Are you sure?');
    })
}

loginCheck();