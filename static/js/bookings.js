const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editButtons = document.getElementsByClassName("edit-btn");
const editConfirm = document.getElementById("saveConfirm");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");


/**
 * Edit booking event listener
 */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.currentTarget.getAttribute("data-booking_id");
    editConfirm.href = `edit_booking/${bookingId}`;
    editModal.show();
  });
}


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