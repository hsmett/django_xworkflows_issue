from django.db import models

from django_xworkflows import models as xwf_models


class TicketWorkflow(xwf_models.Workflow):
    """States and transitions related to :py:class:`Ticket` model."""
    # Disable logging to database.
    log_model = ''
    OPENED = 'OPENED'
    CLOSED = 'CLOSED'

    # List of available states in workflow.
    states = (
        (OPENED, u'opened'),
        (CLOSED, u'closed'),
    )

    # List of available transitions in workflow.
    transitions = (
        ('close', OPENED, CLOSED),
        ('reopen', CLOSED, OPENED),
    )

    # By default, the workflow starts with this state.
    initial_state = OPENED


class Ticket(xwf_models.WorkflowEnabled, models.Model):
    status = xwf_models.StateField(TicketWorkflow)


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
