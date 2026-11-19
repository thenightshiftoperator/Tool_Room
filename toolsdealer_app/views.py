from django.shortcuts import render
from toolsdealer_app.models import *
from django.apps import apps
#MAIN PAGE SELLER
def seller_catalogue(request):
    """Seller catalogue"""
    context = {'tool_operation_choice': tool_operation_choice}
    return render(request, 'toolsdealer_app/root/seller_catalogue.html', context)

def tools(request, toolname):
    """display all tools"""
    if toolname == 'holder':
        field_0 = Holder.objects.all()
        tool_type_list = []

        for i in field_0:
            if i.tool_type in tool_type_list:
                pass
            else:
                tool_type_list.append(i.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }

    elif toolname == 'collet':
        field_0 = Collet.objects.all()
        tool_type_list = []

        for i in field_0:
            if i.tool_type in tool_type_list:
                pass
            else:
                tool_type_list.append(i.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }
    elif toolname == 'mill':
        field_0 = FaceMill.objects.all()
        field_1 = EndMill.objects.all()
        field_2 = BullMill.objects.all()
        field_3 = BallMill.objects.all()
        field_4 = Tcutter.objects.all()
        field_5 = DoveTail.objects.all()
        field_6 = Lollipop.objects.all()
        field_7 = ThreadMill.objects.all()
        field_8 = Engraver.objects.all()
        tool_type_list = []

        if field_0:
            for object in field_0:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_1:
            for object in field_1:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_2:
            for object in field_2:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_3:
            for object in field_3:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_4:
            for object in field_4:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_5:
            for object in field_5:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_6:
            for object in field_6:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_7:
            for object in field_7:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_8:
            for object in field_8:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }
    elif toolname == 'drill':
        field_0 = Drill.objects.all()
        field_1 = SpotDrill.objects.all()
        field_2 = CenterDrill.objects.all()
        field_3 = Tap.objects.all()

        tool_type_list = []

        if field_0:
            for object in field_0:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_1:
            for object in field_1:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_2:
            for object in field_2:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_3:
            for object in field_4:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }
    elif toolname == 'bore':
        field_0 = BoringBar.objects.all()


        tool_type_list = []

        if field_0:
            for object in field_0:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }
    elif toolname == 'tap':
        field_0 = Tap.objects.all()


        tool_type_list = []

        if field_0:
            for object in field_0:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }
    elif toolname == 'saw':
        field_0 = Saw.objects.all()

        tool_type_list = []

        if field_0:
            for object in field_0:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }
    elif toolname == 'turn':
        field_0 = ExternalTurningTool.objects.all()
        field_1 = InternalTurningTool.objects.all()
        field_2 = PartingTool.objects.all()
        field_3 = ThreadingTool.objects.all()

        tool_type_list = []

        if field_0:
            for object in field_0:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_1:
            for object in field_1:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_2:
            for object in field_2:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)
        if field_3:
            for object in field_3:
                if object.tool_type in tool_type_list:
                    pass
                else:
                    tool_type_list.append(object.tool_type)

        context = {'tool_type_list': tool_type_list,
        'toolname': toolname,
        }
    return render(request, 'toolsdealer_app/display/tools.html', context)

def tool(request, toolname, name):
    """Characteristics of the tool."""

    if toolname == 'holder':
        model = Holder.objects.all()
        context = {'model': model, 'name': name}
    elif toolname == 'collet':
        model = Collet.objects.all()
        context = {'model': model, 'name': name}
    elif toolname == 'mill':
        field_0 = FaceMill.objects.all()
        field_1 = EndMill.objects.all()
        field_2 = BullMill.objects.all()
        field_3 = BallMill.objects.all()
        field_4 = Tcutter.objects.all()
        field_5 = DoveTail.objects.all()
        field_6 = Lollipop.objects.all()
        field_7 = ThreadMill.objects.all()
        field_8 = Engraver.objects.all()

        if name == 'face mill':
            context = {'model': field_0, 'name': name}
        elif name == 'end mill':
            context = {'model': field_1, 'name': name}
        elif name == 'bull mill':
            context = {'model': field_2, 'name': name}
        elif name == 'ball mill':
            context = {'model': field_3, 'name': name}
        elif name == 't-cutter':
            context = {'model': field_4, 'name': name}
        elif name == 'dovetail':
            context = {'model': field_5, 'name': name}
        elif name == 'lollipop':
            context = {'model': field_6, 'name': name}
        elif name == 'thread mill':
            context = {'model': field_7, 'name': name}
        elif name == 'engraver':
            context = {'model': field_7, 'name': name}
    elif toolname == 'drill':
        field_0 = Drill.objects.all()
        field_1 = SpotDrill.objects.all()
        field_2 = CenterDrill.objects.all()
        field_3 = Tap.objects.all()

        if name == 'drill':
            context = {'model': field_0, 'name': name}
        elif name == 'spot drill':
            context = {'model': field_1, 'name': name}
        elif name == 'center drill':
            context = {'model': field_2, 'name': name}
        elif name == 'tap':
            context = {'model': field_3, 'name': name}
    elif toolname == 'bore':
        field_0 = BoringBar.objects.all()
        if name == 'boring bar':
            context = {'model': field_0, 'name': name}
    elif toolname == 'tap':
        field_0 = Tap.objects.all()
        if name == 'thread tap':
            context = {'model': field_0, 'name': name}
    elif toolname == 'saw':
        field_0 = Saw.objects.all()
        if name == 'saw':
            context = {'model': field_0, 'name': name}
    elif toolname == 'turn':
        field_0 = ExternalTurningTool.objects.all()
        field_1 = InternalTurningTool.objects.all()
        field_2 = PartingTool.objects.all()
        field_3 = ThreadingTool.objects.all()

        if name == 'external turning':
            context = {'model': field_0, 'name': name}
        elif name == 'internal turning':
            context = {'model': field_1, 'name': name}
        elif name == 'parting tool':
            context = {'model': field_2, 'name': name}
        elif name == 'threading tool':
            context = {'model': field_3, 'name': name}

    return render(request, 'toolsdealer_app/display/tool.html', context)
