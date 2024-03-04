from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = ('<h1>Добро пожаловать в интернет магазин!</h1> \
            <h3>В нашем магазине предоставлен широкий выбор ассортимента</h3> \
            <ul><li>Товары для детей</li> \
                <li>Бытовая техника</li> \
                <li>Товары для дачи</li> \
                <li>Спорт</li> \
                <li>Одежда, обувь</li> \
            </ul>')
    return HttpResponse(html)


def about(request):
    html = ('<h1>О нас</h1> \
            <p>Наш магазин предоставляет товары по лучшим ценам и высокого качества.</p> \
            <p>Магазин находится по адресу 73-й км МКАД</p> \
            <img src="https://www.hotelgreenwood.ru/upload/medialibrary/090/090999d8378bdb9fa481efb6cfb0008e.jpg" alt="Карта проезда"> \
            ')

    logger.info('Успешный вход на страницу')
    return HttpResponse(html)
