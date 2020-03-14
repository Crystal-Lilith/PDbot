const email_copy = () => {
    /* Get the text field */
    var copyText = document.getElementById("email");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    /* Alert the copied text */
    copyText.addEventListener('click', () => {
        /* Copy the text inside the text field */
        document.execCommand("copy");
        Swal.fire({
            position: 'top-start',
            icon: 'success',
            title: 'Copied to clipboard!',
            showConfirmButton: false,
            timer: 1500
        })
    })
}

email_copy();
