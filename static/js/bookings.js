const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editButtons = document.getElementsByClassName("edit-btn");
const editConfirm = document.getElementById("saveConfirm");

const editForm = document.getElementById("edit-booking-form");
const editDate = editForm.querySelector("#id_date");
const editTimeSlot = editForm.querySelector("#id_time_slot");
const editGuests = editForm.querySelector("#id_guests");
const editAllergies = editForm.querySelector("#id_allergies");
const editNotes = editForm.querySelector("#id_booking_notes");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");


/**
 * Edit booking event listener
 */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.currentTarget.getAttribute("data-booking_id");

    // Fetch booking details via AJAX
    fetch(`/booking_list/edit_booking/${bookingId}`)
      .then((response) => response.json())
      .then((data) => {
        editDate.value = data.date;
        editTimeSlot.value = data.time_slot;
        editGuests.value = data.guests;
        editNotes.value = data.booking_notes;

        // Reset allergies checkboxes
        if (editAllergies) {
          let selectedAllergyIds = new Set(data.allergies); // Create a Set of selected allergy IDs for fast lookup

          // Find all the checkboxes and preselect the ones that match the selected allergies
          editAllergies.querySelectorAll("input[type='checkbox']").forEach((checkbox) => {
            checkbox.checked = selectedAllergyIds.has(parseInt(checkbox.value)); // Mark it as checked if its value matches the selected allergy ID
          });
        } else {
          console.warn("Allergies field not found in modal form!");
        }

        // Update the form action to point to the correct booking
        editForm.action = `/booking_list/edit_booking/${bookingId}`;

        // Show the modal
        editModal.show();
        console.log(data.allergies)
      })
        
      .catch((error) => console.error("Error fetching booking:", error));
  });
};


/**
 * Delete booking event listener
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let bookingId = e.currentTarget.getAttribute("data-booking_id");
      deleteConfirm.href = `delete_booking/${bookingId}`;
      deleteModal.show();
    });
  }