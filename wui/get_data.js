    async function make_nd(){
        let dsp = document.querySelector('input[name="dsp_radio"]:checked').value;
        let date = document.getElementById("date_input");
            date.addEventListener("change", function(){});
        let admitting = document.getElementById('admitting_id').value;
        let issuing = document.getElementById('issuing_id').value;
        let approving = document.getElementById('approving_id').value;
        /* let select_list = document.getElementById('select_list').options;
        let selected_date = document.getElementById('date_input');
        selected_date.addEventListener('change', function(){});
        
        let selected_values_list = []

        for (let element of select_list) {
            if(element.selected == true) {
                selected_values_list.push(element.value);
            }
        } */

        await eel.foo(dsp, date.value, admitting, issuing, approving)();
        
        document.getElementById('result').innerHTML = dsp;
        document.getElementById('result_1').innerHTML = date.value;
        document.getElementById('result_2').innerHTML = admitting;
        document.getElementById('result_3').innerHTML = issuing;
        document.getElementById('result_4').innerHTML = approving;
    }

    /* $('#make_nd').click(function(){
        make_nd();
    }) */