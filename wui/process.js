var admittingParent = document.querySelector('p#progress_bar');

eel.expose(progress_bar);
function progress_bar(progress_bar_value) {
    document.getElementById('progr_bar').innerHTML = progress_bar_value
}