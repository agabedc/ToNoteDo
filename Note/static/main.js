function formatUTCtoEST(utcDateTime) {
    // Create a Date object from the UTC datetime string
    const date = new Date(utcDateTime + 'Z');
    
    // Define EST options for formatting
    const options = {
        timeZone: 'America/New_York',
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
        hour: 'numeric',
        minute: '2-digit',
        hour12: true
    };
    
    // Format the date to EST
    return new Intl.DateTimeFormat('en-US', options).format(date);
}

// Apply formatting to all .datetime elements when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const dateTimeSpans = document.querySelectorAll('.datetime');
    dateTimeSpans.forEach(span => {
        const utcDateTime = span.textContent;
        span.textContent = formatUTCtoEST(utcDateTime);
    });
});