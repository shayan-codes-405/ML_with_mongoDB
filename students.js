// Generate 10,000 student records
for (let i = 1; i <= 10000; i++) {

    let attendance = Math.floor(Math.random() * 51) + 50;   // 50-100
    let cgpa = Math.round((Math.random() * 5 + 5) * 100) / 100; // 5.00-10.00
    let studyHours = Math.floor(Math.random() * 9) + 1;     // 1-9
    let internships = Math.floor(Math.random() * 4);       // 0-3

    // Placement based on student performance
    let score = 0;

    if (attendance >= 75) score += 1;
    if (cgpa >= 7) score += 1;
    if (studyHours >= 4) score += 1;
    if (internships >= 1) score += 1;

    let placement = score >= 3 ? "Yes" : "No";

    db.students.insertOne({
        _id: i,
        attendance: attendance,
        cgpa: cgpa,
        studyHours: studyHours,
        internships: internships,
        placement: placement
    });
}

// Check number of records
print("Total students: " + db.students.countDocuments());

// Display first 10 records
db.students.find().limit(10);