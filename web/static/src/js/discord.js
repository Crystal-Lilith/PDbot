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
        if (confirm('Are you sure?')) {
            document.cookie = 'session=;'
            logout();
            location.reload();
        } else {
            location.reload();
        }
    })
}

loginCheck();
