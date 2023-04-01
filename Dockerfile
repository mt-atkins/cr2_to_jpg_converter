FROM python

RUN pip install --upgrade pip 
RUN pip install imageio \
    && pip install rawpy

WORKDIR /images

COPY cr2_to_jpg_converter.py /cr2_to_jpg_converter.py
RUN chmod +x /cr2_to_jpg_converter.py

ENTRYPOINT [ "python", "/cr2_to_jpg_converter.py" ]