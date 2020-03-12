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
        Swal.fire({
            title: 'Confirm',
            text: "Are sure you want to logout?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.value) {
                Swal.fire(
                    'Logging Out!',
                    'You will now be logged out',
                    'success'
                )
                location.replace('https://pden.net/logout');
            }
        });
    })
}

loginCheck();
