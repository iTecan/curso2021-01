from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestHelpdeskFelixrojo(TransactionCase):


    def setUp(self):
        super().setUp()

        self.ticket = self.env["helpdesk.ticket"].create({
            'name': 'Test ticket'
        })
        self.user_id = self.ref('base.user_admin')

    def test_01_ticket(self):
            self.assertEqual(self.ticket.name, "Test ticket")

    def test_02_ticket(self):
            self.assertEqual(self.user_id, self.env['res.users'])
            self.ticket.user_id = self.user_id
            self.assertEqual(self.ticket.user_id, self.user_id)

    def test_03_ticket(self):
            self.assertEqual(self.ticket.name, "Test ticket")
    
    def test_04_ticket(self):
            with self.assertRaises(ValidationError), self.cr.savepoint():
                self.ticket.time = -5