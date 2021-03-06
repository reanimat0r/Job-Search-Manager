from django.db import models
from django.urls import reverse


class Job(models.Model):
    NEW = 'NEW'
    APPLIED = 'APP'
    INTERVIEWING = 'INT'
    AWAITING_DECISION = 'AWD'
    NEGOTIATING_OFFER = 'NGO'
    ACCEPTED_OFFER = 'ACP'
    DECLINED_OFFER = 'DCL'
    STOPPED_PURSUING = 'STP'
    REJECTED = 'REJ'

    company = models.ForeignKey('contacts.Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=3, choices=[
        (NEW, 'New Opportunity'),
        (APPLIED, 'Application Submitted'),
        (INTERVIEWING, 'Interviewing'),
        (AWAITING_DECISION, 'Awaiting Decision'),
        (NEGOTIATING_OFFER, 'Negotiating Offer'),
        (ACCEPTED_OFFER, 'Accepted Offer'),
        (DECLINED_OFFER, 'Declined Offer'),
        (STOPPED_PURSUING, 'Stopped Pursuing'),
        (REJECTED, 'Rejected'),
    ], null=False, blank=False, default=NEW)

    @property
    def is_being_pursued(self):
        return self.status not in (
            self.ACCEPTED_OFFER,
            self.DECLINED_OFFER,
            self.STOPPED_PURSUING,
            self.REJECTED,
        )

    def get_absolute_url(self):
        return reverse('jobs:job_detail', kwargs=dict(pk=self.pk))

    def __str__(self):
        title = self.title
        company = self.company
        return f'{title} @ {company}'
