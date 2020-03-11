function loginCheck() {
    let logButton = document.querySelector('.cta');
    let userName = logButton.text;
    session = document.cookie.split(';')

    logButton.addEventListener('mouseover', () => {
        logButton.text = 'Logout';
    })

    logButton.addEventListener('mouseout', () => {
        logButton.text = userName;
    })

    logButton.addEventListener('click', () => {
        if (confirm('Are you sure?')) {
            document.cookie = "session=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            location.reload();
        } else {
            location.reload();
        }
    })
}

loginCheck();
