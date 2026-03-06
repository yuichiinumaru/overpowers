#!/usr/bin/env node
/**
 * Scaffold a viral quiz template
 */
const fs = require('fs');

const template = `
// Viral Quiz Template
const quizConfig = {
    title: "What Type of Founder Are You?",
    questions: [
        {
            text: "How do you handle stress?",
            options: [
                { text: "Work harder", weight: { typeA: 2, typeB: 0 } },
                { text: "Take a break", weight: { typeA: 0, typeB: 2 } }
            ]
        }
    ],
    results: {
        typeA: { title: "The Hustler", description: "You never stop." },
        typeB: { title: "The Strategist", description: "You think before acting." }
    }
};

function calculateResult(answers) {
    let scores = { typeA: 0, typeB: 0 };
    answers.forEach(ans => {
        scores.typeA += ans.weight.typeA;
        scores.typeB += ans.weight.typeB;
    });
    return scores.typeA > scores.typeB ? "typeA" : "typeB";
}
`;

fs.writeFileSync("quiz_template.js", template.trim());
console.log("Generated quiz_template.js scaffold");
