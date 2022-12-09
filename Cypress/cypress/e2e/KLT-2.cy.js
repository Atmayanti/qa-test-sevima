describe('empty spec', () => {
    // TC-001 
    it('input_less_than_170', () => {
        cy.visit('https://qa.putraprima.id/')
        cy.get('#input').type(12)
        cy.get('#hitung').click()
        cy.get('#result').contains("Faktorial dari ")
    })
    // TC-001 bug
    it('input_more_than_170', () => {
        cy.visit('https://qa.putraprima.id/')
        cy.get('#input').type(171)
        cy.get('#hitung').click()
    })
    // TC-002
    it('input_is_a_float', () => {
        cy.visit('https://qa.putraprima.id/')
        cy.get('#input').type(1.9)
        cy.get('#hitung').click()
        cy.get('#result').should("have.text", "Please enter an integer")
    })
    // TC-003
    it('input_is_a_font', () => {
        cy.visit('https://qa.putraprima.id/')
        cy.get('#input').type("abc")
        cy.get('#hitung').click()
        cy.get('#result').should("have.text", "Please enter an integer")
    })
    // TC-004
    it('input_is_a_special_character', () => {
        cy.visit('https://qa.putraprima.id/')
        cy.get('#input').type("*&^./")
        cy.get('#hitung').click()
        cy.get('#result').should("have.text", "Please enter an integer")
    })
    // TC-005
    it('input_is_empty', () => {
        cy.visit('https://qa.putraprima.id/')
        cy.get('#input').clear()
        cy.get('#hitung').click()
        cy.get('#result').should("have.text", "Please enter an integer")
    })
})