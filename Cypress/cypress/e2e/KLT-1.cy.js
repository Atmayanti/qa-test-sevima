describe('empty spec', () => {
  it('user_can_access_calculator', () => {
    cy.visit('https://qa.putraprima.id/')
    cy.get('.card-header').should("have.text", "Kalkulator Faktorial")
    cy.get('#hitung').contains("Hitung Faktorial").and("be.enabled")
    cy.get('.col-md-6 > :nth-child(2) > :nth-child(1)').contains("Terms Of Service")
    cy.get('.col-md-6 > :nth-child(2) > :nth-child(2)').contains("Privacy Policy")
  })
})