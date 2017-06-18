
class Option():

    def label(self, type=None, **kwargs):
        label_pos = "top"
        if type == "pie":
            label_pos = "outside"
        elif type == "graph":
            label_pos = "inside"
        _label = {"normal": {"show": kwargs.get('label_show', False),
                             "position": label_pos,
                             "textStyle": {"color": kwargs.get('label_text_color', '#000'),
                                           "fontSize": kwargs.get('label_text_size', 12)}}}
        if type != "graph":
            _label.get("normal").update(formatter=kwargs.get('formatter', None))
        return _label

    def color(self, colorlst, **kwargs):
        lc = kwargs.get('label_color', None)
        if lc is not None:
            for color in reversed(list(lc)):
                colorlst.insert(0, color)
        return colorlst

    def line_style(self, **kwargs):
        _line_style = {"normal": {"width": kwargs.get('line_width', 1),
                                  "opacity": kwargs.get('line_opacity', 1),
                                  "type": kwargs.get('line_type', "solid")}}
        return _line_style

    def split_line(self ,**kwargs):
        _split_line = {"show": kwargs.get('split_line_show', True),
                       "lineStyle": Option.line_style(self, **kwargs)}
        return _split_line

    def axis_line(self, **kwargs):
        _axis_line = {"show": kwargs.get('axis_line_show', True),
                      "lineStyle": Option.line_style(self, **kwargs)}
        return _axis_line

    def split_area(self, **kwargs):
        _split_area = {"show": kwargs.get('split_area_show', False),
                       "areaStyle": {"opacity": kwargs.get('split_area_opacity', 1)}}
        return _split_area

    def xy_axis(self, type=None, **kwargs):
        fontsize = kwargs.get('xy_font_size', 14)
        namegap = kwargs.get('nameGap', 25)
        _xAxis = {"name": kwargs.get('xaxis_name', ""),
                  "nameLocation": kwargs.get('xaxis_name_pos', "middle"),
                  "nameGap": namegap,
                  "nameTextStyle": {"fontSize": fontsize},
                  "axisLabel": {"interval": kwargs.get('interval', "auto")}
                 }
        _yAxis = {"name": kwargs.get('yaxis_name', ""),
                  "nameLocation": kwargs.get('yaxis_name_pos', "middle"),
                  "nameGap": namegap,
                  "nameTextStyle": {"fontSize": fontsize}
                 }
        if kwargs.get('exchange', False):
            _yAxis.update(data=kwargs.get('x_axis'), type="category")
            _xAxis.update(type="value")
        else:
            _xAxis.update(data=kwargs.get('x_axis'), type="category")
            _yAxis.update(type="value")
        if type == "scatter":
            _xAxis.update(data=kwargs.get('x_axis'), type="value")
            _yAxis.update(type="value")
        return _xAxis, _yAxis

    def _mark(self, data):
        mark = {"data": []}
        if data is not None:
            for d in list(data):
                if "max" in d:
                    mark.get("data").append({"type": "max", "name": "最大值"})
                elif "min" in d:
                    mark.get("data").append({"type": "min", "name": "最小值"})
                elif "average" in d:
                    mark.get("data").append({"type": "average", "name": "平均值"})
        return mark

    def mark_point(self, **kwargs):
        return self._mark(kwargs.get('mark_point', None))

    def mark_line(self, **kwargs):
        return self._mark(kwargs.get('mark_line', None))

    def cast(self, seq):
        k_lst, v_lst = [], []
        if isinstance(seq, list):
            for s in seq:
                try:
                    if isinstance(s, tuple):
                        k_lst.append(s[0])
                        v_lst.append(s[1])
                except:
                    raise ValueError
        elif isinstance(seq, dict):
            for k, v in seq.items():
                k_lst.append(k)
                v_lst.append(v)
        return k_lst, v_lst