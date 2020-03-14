function email_copy() {
    const el = document.createElement('textarea');
    el.value = 'support@pden.net';
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    Swal.fire({
        icon: 'success',
        title: 'Copied to clipboard!',
        background: '#1d1e22',
        padding: '6rem',
        showConfirmButton: false,
        timer: 1500
    })
}
