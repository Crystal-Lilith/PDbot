function email_copy() {
    const copyText = document.querySelector('.cont');

    copyText.addEventListener('click', () => {
        // /* Select the text field */
        // copyText.select();
        // copyText.setSelectionRange(0, 99999); /*For mobile devices*/

        // /* Copy the text inside the text field */
        // document.execCommand("copy");
        // /* Alert the copied text */
        Swal.fire({
            icon: 'success',
            title: 'Copied to clipboard!',
            background: '#1d1e22',
            padding: '5rem',
            showConfirmButton: false,
            timer: 1500
        })
    })
}
