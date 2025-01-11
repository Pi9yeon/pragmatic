from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail',
                       kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user,
                                                   project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
            
        return super().get(request, *args, **kwargs)
