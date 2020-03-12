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
        function JSconfirm() {
            swal({
                    title: "Confirm",
                    text: "Are sure you want to logout?",
                    type: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#DD6B55",
                    confirmButtonText: "Yes",
                    cancelButtonText: "No",
                    closeOnConfirm: false,
                    closeOnCancel: false
                },
                function (isConfirm) {
                    if (isConfirm) {
                        swal("Logged out", "success");
                        location.replace('https://pden.net/logout');
                    }
                });
        }
    })
}

loginCheck();
