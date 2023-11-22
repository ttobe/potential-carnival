import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { NestExpressApplication } from '@nestjs/platform-express'
import { join } from 'path';
import { setupSwagger } from './swagger';

async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule);
  
  app.useStaticAssets(join(__dirname, "..", "static"));
  app.setBaseViewsDir(join(__dirname, "..", "views"));
  app.setViewEngine('hbs')
  setupSwagger(app);
  await app.listen(3000);
}
bootstrap();
