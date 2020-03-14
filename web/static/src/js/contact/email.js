function email_copy() {
    /* Get the text field */
    const copyText = document.querySelector('#email');

    copyText.addEventListener('click', () => {      
        /* Select the text field */
        copyText.select(); 
        
        /* Copy the text inside the text field */
        document.execCommand("copy"); 
        // /* Alert the copied text */
        Swal.fire({
            icon: 'success',
            title: 'Copied to clipboard!',
            background: '#1d1e22',
            padding: '6rem',
            showConfirmButton: false,
            timer: 1500
        })
    })
}
