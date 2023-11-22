import { Controller, Get, Post, Body, Patch, Param, Delete, Render } from '@nestjs/common';
import { MapService } from './map.service';
import { CreateMapDto } from './dto/create-map.dto';
import { UpdateMapDto } from './dto/update-map.dto';

@Controller('map')
export class MapController {
  constructor(private readonly mapService: MapService) { }

  @Post()
  create(@Body() createMapDto: CreateMapDto) {
    return this.mapService.create(createMapDto);
  }

  @Get()
  @Render('map.hbs')
  findAll() {
  }


  @Get('/detail')
  @Render('detail.hbs')
  detail() {
  }


  @Patch(':id')
  update(@Param('id') id: string, @Body() updateMapDto: UpdateMapDto) {
    return this.mapService.update(+id, updateMapDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.mapService.remove(+id);
  }
}
