const editButtons = document.getElementsByClassName("edit-btn");


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let bookingId = e.currentTarget.getAttribute("data-booking_id");
      deleteConfirm.href = `delete_booking/${bookingId}`;
      deleteModal.show();
    });
  }