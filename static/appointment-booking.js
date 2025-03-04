(function () {
    const API_BASE_URL = "http://127.0.0.1:8000"; // Change this to your API base URL

    function createBookingUI(container) {
        container.innerHTML = `
            <div id="booking-container">
                <h3>Book an Appointment</h3>
                <label for="booking-date">Select Date:</label>
                <input type="date" id="booking-date" min="${new Date().toISOString().split('T')[0]}" required>

                <label for="booking-time">Select Time Slot:</label>
                <select id="booking-time" disabled required>
                    <option value="">Select a time slot</option>
                </select>

                <label for="name">Your Name:</label>
                <input type="text" id="name" placeholder="Enter your name" required>

                <label for="phone">Phone Number:</label>
                <input type="text" id="phone" placeholder="Enter phone number" required>

                <button id="book-appointment">Book Appointment</button>
                <p id="booking-message"></p>
            </div>
        `;

        document.getElementById("booking-date").addEventListener("change", fetchAvailableSlots);
        document.getElementById("book-appointment").addEventListener("click", bookAppointment);
    }

    function fetchAvailableSlots() {
        const date = document.getElementById("booking-date").value;
        if (!date) return;

        fetch(`${API_BASE_URL}/api/available-slots/?date=${date}`)
            .then(response => response.json())
            .then(data => {
                const timeSelect = document.getElementById("booking-time");
                timeSelect.innerHTML = `<option value="">Select a time slot</option>`;
                data.available_slots.forEach(slot => {
                    const option = document.createElement("option");
                    option.value = slot;
                    option.textContent = slot;
                    timeSelect.appendChild(option);
                });
                timeSelect.disabled = false;
            })
            .catch(error => console.error("Error fetching slots:", error));
    }

    function bookAppointment() {
        const name = document.getElementById("name").value;
        const phone = document.getElementById("phone").value;
        const date = document.getElementById("booking-date").value;
        const timeSlot = document.getElementById("booking-time").value;
        const message = document.getElementById("booking-message");

        if (!name || !phone || !date || !timeSlot) {
            message.textContent = "All fields are required!";
            return;
        }

        const appointmentData = { name, phone_number: phone, date, time_slot: timeSlot };

        fetch(`${API_BASE_URL}/api/book-appointment/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(appointmentData),
        })
            .then(response => response.json())
            .then(data => {
                if (data.id) {
                    message.textContent = "Appointment booked successfully!";
                    message.style.color = "green";
                } else {
                    message.textContent = data.error || "Booking failed!";
                    message.style.color = "red";
                }
            })
            .catch(error => console.error("Error booking appointment:", error));
    }

    window.EmbedBookingWidget = function (containerId) {
        const container = document.getElementById(containerId);
        if (container) createBookingUI(container);
    };
})();
