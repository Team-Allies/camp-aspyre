console.log("main.js loaded")


let button = document.getElementById('button_for_medications')

function add_new_div() {
  button.addEventListener('click', function(event) {
    console.log("yeet");
    let newdiv = document.createElement("div");
    newdiv.innerHTML =
      `<div class="text_field">
        <h5 class="field_title">Medication:</h5>
          {{ form.sixth_medication_name }}
        </div>
        <div class="text_field">
          <h5 class="field_title">Dose:</h5>
          {{ form.sixth_medication_dose }}
        </div>
        <div class="text_field">
          <h5 class="field_title">Take at what times:</h5>
          {{ form.sixth_medication_times }}
        </div>
        <div class="text_field">
          <h5 class="field_title">Reasons for Taking:</h5>
          {{ form.sixth_medication_reason_for_taking }}
        </div>
        <div class="text_field">
          <h5 class="field_title">Prescriber:</h5>
          {{ form.sixth_medication_prescriber_name }}
        </div>
        <div class="text_field">
          <h5 class="field_title">Prescriber's Phone Number:</h5>
          {{ form.sixth_medication_prescriber_phone_number }}
        </div>
      </div>`;
    document.body.appendChild(newdiv);
  })
}

add_new_div()

// let medicationBoolean = document.getElementById('medications_boolean')
// function add_new_div() {
//   medicationBoolean.addEventListener('click', function(event) {
//     console.log("yeet");
//     let newdiv = document.createElement("div");
//     let booleanField = document.getElementById("medications_boolean");
//     if (booleanField.checked) {
//       newdiv.innerHTML =
//         `<div class="text_field">
//       <h5 class="field_title">Medication:</h5>
//         {{ form.sixth_medication_name }}
//       </div>
//       <div class="text_field">
//         <h5 class="field_title">Dose:</h5>
//         {{ form.sixth_medication_dose }}
//       </div>
//       <div class="text_field">
//         <h5 class="field_title">Take at what times:</h5>
//         {{ form.sixth_medication_times }}
//       </div>
//       <div class="text_field">
//         <h5 class="field_title">Reasons for Taking:</h5>
//         {{ form.sixth_medication_reason_for_taking }}
//       </div>
//       <div class="text_field">
//         <h5 class="field_title">Prescriber:</h5>
//         {{ form.sixth_medication_prescriber_name }}
//       </div>
//       <div class="text_field">
//         <h5 class="field_title">Prescriber's Phone Number:</h5>
//         {{ form.sixth_medication_prescriber_phone_number }}
//       </div>
//     </div>`;
//     }
//     document.body.appendChild(newdiv);
//   })
// }
// add_new_div()