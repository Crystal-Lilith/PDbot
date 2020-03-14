const email_copy = () => {
    /* Get the text field */
    var copyText = document.getElementById("cta");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    copyText.addEventListener('click', () => {
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
