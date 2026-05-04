describe('Product Catalogue Admin UI', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000')
  })

  it('displays the correct page header', () => {
    cy.get('h1').should('contain', 'Product Store Admin')
  })

  it('can search for products', () => {
    cy.get('#product_name').type('Fedora')
    cy.get('#search-btn').click()
    cy.get('#flash_message').should('contain', 'Success')
    cy.get('#search_results').should('contain', 'Fedora')
  })

  it('clears the form correctly', () => {
    cy.get('#product_name').type('Temporary Data')
    cy.get('#clear-btn').click()
    cy.get('#product_name').should('have.value', '')
    cy.get('#flash_message').should('contain', 'Cleared')
  })
})
