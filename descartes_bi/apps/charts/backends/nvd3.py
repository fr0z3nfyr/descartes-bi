from __future__ import absolute_import

import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from .base import ChartBackend


class NovusD3(ChartBackend):
    label = _('Novus D3')

    options = {
        'name': 'chart_type',
        'label': _('chart type'),
        'choices': (
            ('SI', _('Standard X,Y')),
            ('SH', _('Horizontal X,Y')),
            ('PI', _('Pie chart')),
            ('LB', _('Line Plus Bar Chart')),
            ('LI', _('Line chart')),
            ('LF', _('Line chart with Focus')),
        )
    }

    def render(self, report, request):
        series_results = report.execute(request)
        context = {
            'series_results': [json.dumps(result) for result in series_results],
            'report': report,
            'chart_type': 'LI',
        }

        return render_to_response('charts/novus/merged.html', context,
            context_instance=RequestContext(request))
