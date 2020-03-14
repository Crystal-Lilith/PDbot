function email_copy() {
    const copyText = document.getElementById('#email');

    copyText.addEventListener('click', () => {
        /* Select the text field */
        copyText.select();
        copyText.setSelectionRange(0, 99999); /*For mobile devices*/

        /* Copy the text inside the text field */
        document.execCommand("copy");
        /* Alert the copied text */
        Swal.fire({
            position: 'top-start',
            icon: 'success',
            title: 'Copied to clipboard!',
            showConfirmButton: false,
            timer: 1500
        })
    })
}
