import { TestBed } from '@angular/core/testing';

import { IntercomponentSignalerService } from './intercomponent-signaler.service';

describe('IntercomponentSignalerService', () => {
  let service: IntercomponentSignalerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(IntercomponentSignalerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
